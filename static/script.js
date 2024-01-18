let watchlistButtonClickListener;
let watchlist = JSON.parse(localStorage.getItem('watchlist')) || [];

//load watchlist from db
//populate quote/change
//display Watchlist on DOM
//update price/change every 15 seconds while on the page

//add watchlist ticker to db
//remove watchlist ticker from db
//error handling for blank tickers
//advise user to enter crypto as BTC-US SOL-US etc
//create default watchlist with equity and crypto and FX



async function retrieveQuote() {
  let user_input = document.getElementById('ticker');
  let ticker = user_input.value.toUpperCase();
  user_input.value = '';
  if (ticker === '') {
    // Handle empty input (e.g., display an alert or a warning message)
    alert('Input cannot be empty');
    return; // Stop the function if the input is empty
  }
  //check api for vaid ticker
  try {
    let url = `http://127.0.0.1:5000/quote/${ticker}`;
    response = await axios.get(url);

    return displayQuote(response, ticker);

  } catch {
    alert('invalid ticker');
    return 1;
  }

};

function displayQuote(response, ticker) {

  const displayContainer = document.getElementById('quote-section');
  document.getElementById('symbolField').textContent = ticker;
  document.getElementById("priceField").textContent = response.data.regularMarketPrice;
  document.getElementById('changeField').textContent = response.data.regularMarketChange;
  document.getElementById('Pctchange').textContent = response.data.regularMarketChangePercent;
  document.getElementById('nameField').textContent = response.data.shortName;

  const watchlistButton = document.getElementById('add');
  watchlistButton.removeEventListener('click', watchlistButtonClickListener);

  // Attach a new click event listener
  watchlistButtonClickListener = () => addToWatchlist(response.data, ticker);
  watchlistButton.addEventListener('click', watchlistButtonClickListener);

  function handleWatchlistButtonClick(data, ticker) {
    // Call addToWatchlist with the correct parameters
    watchlistButton.removeEventListener('click', handleWatchlistButtonClick);
    addToWatchlist(data, ticker);
  }
}



function addToWatchlist(data, ticker) {

  if (watchlist.includes(ticker)) {
    alert('already in watchlist');
    const watchlistButton = document.getElementById('add');
    watchlistButton.removeEventListener('click', watchlistButtonClickListener);

    return;
  } else {
    watchlist.push(ticker);
    localStorage.setItem('watchlist', JSON.stringify(watchlist));


    return displayQuoteInWatchlist(ticker, data);
  }

}

function displayQuoteInWatchlist(ticker, data) {
  let table = document.getElementById('watchlist-table');
  const row = document.createElement('tr');
  const symbolCell = document.createElement('td');
  symbolCell.textContent = ticker;
  row.appendChild(symbolCell);

  const priceCell = document.createElement('td');
  priceCell.textContent = data.regularMarketPrice;
  row.appendChild(priceCell);

  const changeCell = document.createElement('td');
  changeCell.textContent = data.regularMarketChange;
  row.appendChild(changeCell);

  const PctchangeCell = document.createElement('td');
  PctchangeCell.textContent = data.regularMarketChangePercent;
  row.appendChild(PctchangeCell);


  const nameCell = document.createElement('td');
  nameCell.textContent = data.shortName;
  row.appendChild(nameCell);

  let removeButton = document.createElement('button');
  removeButton.textContent = 'Remove';

  removeButton.id = 'remove';
  row.appendChild(removeButton);
  removeButton.onclick = function () {
    removeTickerFromDOMAndLocalStorage(row, ticker);
  };

  table.appendChild(row);
  updateWatchlist(watchlist);

}



document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
  const quoteButton = document.getElementById('quote');

  // Add click event listener to the button
  quoteButton.addEventListener('click', (event) => {
    // Prevent the default action of the event (e.g., form submission)
    event.preventDefault();

    // Call the validateTicker function
    retrieveQuote();
  });
});


function removeTickerFromDOMAndLocalStorage(row, ticker) {
  row.parentNode.removeChild(row);
  watchlist = watchlist.filter(symbol => symbol !== ticker);
  localStorage.setItem('watchlist', JSON.stringify(watchlist));
  console.log('remove', row, ticker);


  // need to send  DELETE ticker to backend

}





document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
  const removeButton = document.getElementById('remove');

  // Add click event listener to the button
  removeButton.addEventListener('click', (event) => {
    // Prevent the default action of the event (e.g., form submission)
    event.preventDefault();

    // Call the validateTicker function
    removeTicker();
  });
});


function updateWatchlist(watchlist) {

 let url = 'http://127.0.0.1:5000/update_watchlist';
   axios.post(url, watchlist)
   .then(response => {
    console.log('Response from server:', response.data)
   });





  // } catch {
  //   console.log('error with watchlist');
  //   return 1;
  // }
 ;
}