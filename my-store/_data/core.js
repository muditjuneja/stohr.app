module.exports = function () {
    return {
        environment: process.env.MY_ENVIRONMENT || "development",
        backend: process.env.BACKEND || "http://localhost:8003",
        formEndpoint: process.env.FORM_ENDPOINT || "submit-query",
    };
};