#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    if (searchElement) {
    for(let i = 0; i < list.length; i++) {
        if (searchElement == list[i]) {
            count++;
        }
    }
}
    return count;
}