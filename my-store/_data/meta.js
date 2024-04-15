const metaJson = require('./_meta.json');

const data = [...metaJson];
module.exports = () => {
    let _obj = {};
    for (let m of data) {
        console.log("nm", m);
        const key = m.field.replace(/[: ]/g, '_').toLowerCase();

        if (key == 'hero_images') {
            _obj[key] = m.value.split(',');
        } else {
            _obj[key] = m.value;
        }
    }

    console.log("_obj", _obj);
    return _obj;
};