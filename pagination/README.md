
#  Pagination
---

#   Pagination Patterns in REST APIs  
A practical exploration of three essential pagination strategies:  
**simple page/page_size**, **hypermedia-driven pagination**, and **deletion‑resilient cursor pagination**.

---

##   Overview  
This project provides a structured guide and implementation patterns for building robust, scalable, and developer‑friendly pagination in REST APIs.  

Pagination is a foundational part of API design because returning large datasets without limits can cause excessive network usage, slow queries, and poor user experience. As noted in the Moesif API design document:  
> “Most endpoints that return a list of entities will need to have some sort of pagination.”   

We explore three complementary approaches:

1. **Simple page/page_size pagination** — easy to implement, ideal for small datasets.  
2. **Hypermedia (HATEOAS) pagination** — self‑describing navigation using links.  
3. **Deletion‑resilient pagination** — cursor/seek‑based pagination that avoids page drift.

Each method includes examples, pros/cons, and references.

---

##   Core Questions Addressed  
These are included *exactly* as you requested:

1. **How to paginate a dataset with simple page and page_size parameters**  
2. **How to paginate a dataset with hypermedia metadata**  
3. **How to paginate in a deletion-resilient manner**

---

## 1 Paginate with `page` and `page_size`  
This is the classic **offset pagination** pattern.

###    Concept  
Compute offset as:  
\[
\text{offset} = (\text{page} - 1) \cdot \text{page\_size}
\]

###    Example  
```
GET /items?page=3&page_size=20
```

Backend logic:
```
offset = (3 - 1) * 20 = 40
SELECT * FROM items ORDER BY id LIMIT 20 OFFSET 40;
```

###    Pros  
- Very easy to implement  
- Stateless  
- Works with any sorting

###    Cons  
- Slow for large offsets  
- Page drift when items are inserted/deleted  
  > “Not consistent when new items are inserted… Page drift.” 

---

##    Paginate with Hypermedia Metadata (HATEOAS)  
Hypermedia-driven APIs embed navigation links directly in the response.  
From the HATEOAS document:  
> “Subsequent requests the user-agent may make are discovered inside the response to each request.” 

###    Example Response  
```
{
  "items": [...],
  "page": 3,
  "page_size": 20,
  "links": {
    "self": "/items?page=3&page_size=20",
    "next": "/items?page=4&page_size=20",
    "prev": "/items?page=2&page_size=20"
  }
}
```

###    Pros  
- Self-describing navigation  
- Client does not need to know URL structure  
- Server can evolve independently

###    Cons  
- Slightly more work to generate links  
- Still suffers from offset drift unless combined with cursor pagination

---

##    Deletion‑Resilient Pagination (Cursor / Seek Pagination)  
Cursor-based pagination avoids page drift by using a stable reference (ID or timestamp) instead of page numbers.

From the Moesif document:  
> “Seek Paging… ensures consistent ordering even when newer items are inserted.” 

###    Example  
First request:
```
GET /items?limit=20
```

Response:
```
"next_cursor": "last_item_id"
```

Next request:
```
GET /items?limit=20&after_id=12345
```

###    Pros  
- No page drift  
- Fast for large datasets  
- Stable ordering  
- Works well with insertions/deletions

###    Cons  
- Requires a stable indexed field  
- More complex backend logic when sorting by non-ID fields

---

##  Example Theme: “Items API”  
Below is a simple conceptual API that supports all three pagination modes.

### Endpoints  
- `/items?page=1&page_size=20` — offset pagination  
- `/items?page=1&page_size=20` with HATEOAS links  
- `/items?limit=20&after_id=100` — cursor pagination  

### Sample Response (Cursor)  
```
{
  "items": [...],
  "limit": 20,
  "next_cursor": "140",
  "links": {
    "next": "/items?limit=20&after_id=140"
  }
}
```

---

##   References  
These explanations are grounded in your uploaded documents:

- **REST API Design: Filtering, Sorting, and Pagination — Moesif**  
  (Pagination types, offset drift, keyset, seek pagination)  
  > “Seek Paging… ensures consistent performance even with large offsets.” 

- **HATEOAS — Wikipedia**  
  (Hypermedia-driven navigation)  
  > “RESTful interaction is driven by hypermedia, rather than out-of-band information.” 

---
# Author :Eugenio Martinez
