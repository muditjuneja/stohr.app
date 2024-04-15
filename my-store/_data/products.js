// const catJson = require('./_categories.json');
const productsJson = require('./_products.json');

const data = [...productsJson];
module.exports = () => {
    data.forEach(product => {
        // product.img = product['Image Src'];
    });

    return data;
};