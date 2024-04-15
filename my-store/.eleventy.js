// eleventy --serve

module.exports = function (eleventyConfig) {

    eleventyConfig.addPassthroughCopy("images");

    eleventyConfig.addFilter("jsonStringify", function (value) {
        return JSON.stringify(value);
    });
    // eleventyConfig.addPassthroughCopy("src/styles.css"); // If you have a CSS file
    // eleventyConfig.useTimestampStatus = false; 

    // Add a find filter
    // eleventyConfig.addFilter("find", function(array, testFn) {
    //     return array.find(testFn);
    // });

    // Add a collection for products
    // eleventyConfig.addCollection("products", function(collectionApi) {
    //     return require("./src/products.json");
    // });

    // return {
    //     dir: {
    //         input: "src", // Or wherever your source files are
    //         includes: "../_includes", // Or wherever your includes files are
    //         output: "_site" // Or wherever you want the output to go
    //     }
    // };
};