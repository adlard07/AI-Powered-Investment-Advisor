## AI Powered Investment Advisor
```
Unlock smarter investing with our **AI-Powered Financial Advisor**! Stay ahead of the market with real-time news analysis, stock updates, and expert recommendations tailored to your goals. From **forecasting future trends** to optimizing your portfolio across stocks, mutual funds, gold, and more, our cutting-edge system delivers the best strategies for your unique needs. Powered by **advanced AI and attention models**, it simplifies complex decisions while maximizing returns. With an intuitive interface and secure deployment on **Azure**, investing has never been this easy or efficient. Start today and take control of your financial future—your perfect portfolio is just a click away!
```
### Folder Structure
```
financial-advisor-system/
│── build/
│    ├── data_ingestion
│    │   ├── chroma_db.py
│    │   ├── get_data.py
│    ├── model_building
│    │   ├── build_model.py
│    ├── pipeline
│    │   ├── database_pipeline.py
│    ├── utils
│    │   ├── utils.py
│    │   ├── logger.py
│   database/
│       ├── chroma.sqlite3
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── user_management.py
│   │   ├── portfolio_optimization.py
│   │   ├── sentiment_analysis.py
│   │   ├── data_pipeline.py
│   │   ├── forecasting.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── sentiment_model.py
│   │   ├── forecasting_model.py
│   │   ├── optimization_model.py
│   ├── utils/
│   │   ├── news_fetcher.py
│   │   ├── stock_price_fetcher.py
│   │   ├── azure_connector.py
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── InvestmentForm.jsx
│   │   │   ├── PortfolioRecommendation.jsx
│   │   ├── App.js
│   │   ├── index.js
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
├── data/
│   ├── raw/
│   ├── processed/
│   ├── logs/
├── tests/
│   ├── test_api.py
│   ├── test_models.py
│   ├── test_utils.py
├── README.md
├── .gitignore
```
### Project Flow

1. **Data Ingestion**:
   - The project begins with data ingestion through the **Kaggle API**, which pulls relevant financial data from Kaggle's datasets. This data is then processed and stored in **ChromaDB** using `chroma_db.py`.
   
2. **Data Analysis**:
   - The stored data in ChromaDB is queried and used for **data analysis** in **R**. Insights from the analysis are extracted and compiled into a comprehensive report.
   
3. **Sentiment Analysis**:
   - Once the insights are generated, the data is used to build a **Sentiment Analysis Model**. To enhance the accuracy and efficiency of sentiment classification, two architectures are chosen:
     - **BiLSTM (Bidirectional LSTM)** model, which is well-suited for sequential data like financial text.
     - **BERT (Bidirectional Encoder Representations from Transformers)**, specifically the pretrained model **"ProsusAI/finbert"**, which is optimized for financial data.
   
4. **Model Evaluation and Deployment**:
   - Both models are trained and evaluated based on their performance, efficiency, and lightweight characteristics. The model that offers the **best balance of accuracy**, **efficiency**, and **low resource usage** is selected for deployment.
   - The chosen model is then deployed in a secure environment, leveraging **Azure** for scaling and robust management.

With this architecture, the AI-powered system is designed to provide optimal investment insights through sentiment analysis and data-driven forecasting, helping users make informed decisions in the financial market.