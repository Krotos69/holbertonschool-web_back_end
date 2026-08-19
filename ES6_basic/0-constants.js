// 0-constants.js

export function taskFirst() {
	const task = 'I prefer const when I can.';
	return task;
}

export function getlast() {
	return ' is okay';
}

export function tasknext() {
	let combination = 'But sometimes let';
	combiantion += getlast();
	return combination;
}
