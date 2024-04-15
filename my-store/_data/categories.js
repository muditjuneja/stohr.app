const catJson = require('./_categories.json');
const productsJson = require('./_products.json');

const data = [...catJson];
module.exports = () => {
  data.forEach(category => {
    category.products = productsJson.filter(x => x.Type == category.name);

    // TODO - Move this out of this file
    category.products.forEach(x => {
      x.img = x['Image Src']
    })
  });

  return data;
};