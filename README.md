**Stohr: The open-source e-commerce platform powered by Google Sheets**

Build a beautiful, functional online store in minutes - no coding required. Stohr connects seamlessly with your Google Sheets, transforming your product data into a customizable e-commerce website.

**Key Features**

* **Effortless Setup:** Get your store up and running without writing a line of code.
* **Google Sheets Integration:**  Manage your products, categories, and metadata directly in familiar spreadsheets. 
* **Community-Driven:** Contribute to Stohr's development and shape its future.
* **Query Management:** Collect and manage customer queries directly from your spreadsheet.
* **Customization:**  Tailor your storefront with templates and styling options (coming soon!).
* **Payment Gateway:** Collect and manage payment entires directly in your sheet (coming soon!).


**Stohr vs. Traditional Development**

Let's break down the difference in time investment for common e-commerce tasks:

| Task                                 | Traditional Development | Stohr                                   |
|--------------------------------------|-------------------------|-----------------------------------------|
| Setting up emails                    | 2-6+ hrs                | Potentially 0 hrs, dependent on needs     |
| Designing a landing page             | 4-10+ hrs               |  Hours, depending on template use        |
| Handling payment webhooks            | 2-5+ hrs                | Integration needed, complexity varies     |
| Managing SEO tags                    | 1-3+ hrs                |  Simplified with frontend integration      |
| Setting up Google OAuth              | 1-2+ hrs                |  Streamlined with Google Sheets focus    |
| Configuring DNS records              | 1-2+ hrs                | May be less complex                     |
| Building & protecting API routes     | 2-5+ hrs                |  May be minimized or unnecessary         |
| **Overthinking the technical stuff** | ∞ hrs                   | Drastically reduced                    |

**The Stohr Advantage**

Stohr's core mission is to empower you to focus on your *business* rather than fighting technical battles. While traditional development offers flexibility, it comes with a significant time cost. Stohr aims to streamline the process and get your online store up and running faster.


**Getting Started**

1. **Create a Google Sheet:** 
    * Download the sample workbook from [here](https://docs.google.com/spreadsheets/d/14gC0luUCl6aAVfm6T3J0ekvsGqCnWDlSAEoQzsJH7FQ/edit?usp=sharing). This include the following sheets - 
        * meta - this is the basic information about your store like store name, address, instagram page etc
        * categories - this is used to manage categories accorss product ranges
        * products - this is the core of the site and includes meta data for the products you want to list in your store.
    * Upload the sheet from [Step 1] to your google account
2. **Create a service account:** Follow [this guide](https://cloud.google.com/iam/docs/service-accounts-create) to create a service account. You may need to create a new project in your account.
3. **Enable Google Sheets API:** Visit Google cloud marketplace to enable Google Sheets API. [Navigate here](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com)

4. **Set Environment Variables**
    * `CREDENTIALS_FILE`: Path to your credentials JSON file.
    * `SPREADSHEET_ID`: The unique ID of your Google Sheet.
    * `QUERY_SHEET`: The name of the sheet within your spreadsheet where customer queries will be stored.
4. **Install Stohr:** (Instructions for cloning your repository)
5. **Deploy Your Frontend**
    * Stohr offers flexibility - use your favorite frontend framework or choose a Vercel integration for simplified deployment (Vercel adapter included).

**Customization (Coming Soon)**

* **Templates:**  Select from a range of pre-designed templates to get started quickly.
* **CSS Styling:** Style your store's appearance to match your brand.

**How Stohr Works**

1. Stohr reads data from your designated Google Sheets.
2. It transforms this data into a structured e-commerce format.
3. Stohr creates a store for you in the background and keeps the data in sync. Each time, it detects changes, it triggers a new deployment of your store so that updates you make in your spreadsheet are automatically reflected on your live site.

**Join the Community**

Stohr is an open-source project driven by its users. We welcome your contributions, feedback, and ideas!

* **GitHub Repository:** [[invalid URL removed]]
* **Discussions:** (Consider a forum or dedicated Discord channel)
* **Report Issues:** [Include a link to the Issue Tracker on your repo]

**Let's build the future of spreadsheet-powered e-commerce together!** 


