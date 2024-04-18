// simple code snippet for counting edges in an SVG
// this is useful in case you want to compare what Moose shows you and the arch map SVG it generates
var count = 0
var allPaths = document.querySelectorAll("path")

for (path of allPaths) {
    if (path.getAttribute("style").indexOf("stroke:#000000") > -1 && path.getAttribute("style").indexOf("stroke-linecap:butt") > -1) {
        count++
    }
}

console.log(count)