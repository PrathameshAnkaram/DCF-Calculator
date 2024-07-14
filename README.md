## Introduction
The DCF (Discounted Cash Flow) Model Dashboard is an interactive tool designed to provide users with a dynamic way to estimate the intrinsic value of publicly traded companies. By allowing real-time adjustments of the financial assumptions such as growth rate, discount rate, and the investment horizon, this dashboard aids in making informed investment decisions based on the calculated DCF values.

## Features
- **Dynamic Input Adjustment**: Users can modify the growth rate, discount rate, and the number of years to forecast, seeing instantly how these changes affect the company's valuation.
- **Real-Time Data Fetching**: Utilizes `yfinance` to fetch real-time financial data from Yahoo Finance.
- **Interactive Visualization**: Includes a graph that dynamically updates to show future cash flows and their present values based on user inputs.
- **User-Friendly Interface**: Designed with simplicity and ease of use in mind, making financial analysis accessible to both novices and experienced investors.

## Technologies Used
- **Python**: The core programming language used.
- **Dash**: A Python framework for building analytical web applications.
- **Plotly**: For creating interactive plots.
- **YFinance**: To fetch live financial data.
