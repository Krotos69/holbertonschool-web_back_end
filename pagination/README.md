Here’s the concise core answer up front:

**Simple page/page_size pagination uses offset math (`offset = page * page_size`).  
Hypermedia pagination wraps the page in metadata and navigational links (HATEOAS).  
Deletion‑resilient pagination uses stable cursors (usually item IDs or timestamps) instead of page numbers.**

Below, I expand each method with structure, examples, trade-offs, and practical implementation guidance.

---

## 1) Paginating with simple `page` and `page_size` parameters  
This is the classic **offset pagination** pattern.

### Core idea  
Compute the offset as:
\[
\text{offset} = (\text{page} - 1) \cdot \text{page\_size}
\]

Then return:
- the slice of data  
- metadata about the current page  
- optionally next/previous page numbers

### Example  
```
GET /items?page=3&page_size=20
```
Backend:
```
offset = (3 - 1) * 20 = 40
SELECT * FROM items ORDER BY id LIMIT 20 OFFSET 40;
```

### Pros  
- Very easy to implement  
- Works with arbitrary sorting  
- Stateless

### Cons  
- Slow for large offsets (DB must scan/skip rows)  
- **Page drift**: if items are inserted or deleted, page boundaries shift  
  (document confirms this: “Not consistent when new items are inserted… Page drift” )

---

## 2) Paginating with hypermedia metadata (HATEOAS style)  
Here you return not only the data but also **links** describing how to navigate to the next/previous pages.  
This follows the REST constraint “Hypermedia as the Engine of Application State” (HATEOAS).

### Core idea  
The server includes navigation links inside the response so the client does not need to know URL patterns.

### Example response  
```
HTTP/1.1 200 OK
{
  "items": [...],
  "page": 3,
  "page_size": 20,
  "total": 240,
  "links": {
    "self": "/items?page=3&page_size=20",
    "next": "/items?page=4&page_size=20",
    "prev": "/items?page=2&page_size=20"
  }
}
```

This mirrors the pattern described in the HATEOAS document:  
“Subsequent requests the user-agent may make are discovered inside the response to each request.” 

### Pros  
- Client does not hardcode URL structure  
- Server can evolve without breaking clients  
- Clear navigation semantics

### Cons  
- Slightly more work on the server  
- Still suffers from offset problems unless combined with cursor-based pagination

---

## 3) Deletion‑resilient pagination (cursor/seek pagination)  
This is the **correct** way to avoid page drift and deletion issues.  
Instead of page numbers, you use a **cursor** (usually a unique, ordered field like `id` or `created_at`).

### Core idea  
Return items **after** a certain cursor value.  
The cursor is typically the last item’s ID or timestamp from the previous page.

### Example  
First request:
```
GET /items?limit=20
```
Response includes:
```
"next_cursor": "last_item_id"
```

Next request:
```
GET /items?limit=20&after_id=12345
```

This is exactly what the document calls **Seek Pagination**:  
“By adding an after_id or start_id URL parameter, we can remove the tight coupling of paging to filters and sorting.”  
“If items are deleted… the start_id may not be a valid id.” (but the pagination still works because you seek forward)  


### Why this is deletion‑resilient  
If items are deleted, the cursor still points to a stable position in the ordered dataset.  
You are not relying on row counts or offsets.

### Pros  
- No page drift  
- Fast even for large datasets  
- Works well with insertions and deletions  
- Stable ordering

### Cons  
- Requires a stable, indexed sort key  
- More complex backend logic when sorting by non-ID fields

---

## Summary Table

| Method | Best for | Pros | Cons |
|-------|----------|------|------|
| **Offset (page/page_size)** | Small datasets, simple apps | Easy, flexible | Slow for large offsets, page drift |
| **Hypermedia pagination** | REST/HATEOAS APIs | Self-describing navigation | Still offset-based unless combined with cursors |
| **Cursor/Seek pagination** | Large datasets, deletion-resilient APIs | Fast, stable, no drift | Requires stable sort key, more backend logic |

---

## What you might want next  
Would you like me to show:

- code examples in Python/Node/Go?  
- API response schemas for each pagination style?  
- How to combine filtering%2C sorting%2C and pagination into one endpoint?