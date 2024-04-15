const express = require('express');
const path = require('path');
const app = express();

const _siteDir = '..';
// Define the path to the "public" directory
const sitePath = path.join(__dirname, _siteDir, '_site');

// Serve static files from the "public" directory
app.use(express.static(sitePath));

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});