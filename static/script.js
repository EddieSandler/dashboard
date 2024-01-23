let watchlistButtonClickListener;
let watchlist = JSON.parse(sessionStorage.getItem('watchlist')) || [];
const userId = document.getElementById('userId').textContent;
console.log(userId);
//.getAttribute('data-user-id');
console.log(userId);

// localStorage.setItem('user', JSON.stringify(userId));


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
  let ticker_type = response.data.quoteType;
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
  console.log(ticker)
  console.log(data.shortName)
  console.log(data.quoteType)
  console.log(userId)


  return addTickerToDatabase(ticker, data.shortName,data.quoteType, userId);


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
  sessionStorage.setItem('watchlist', JSON.stringify(watchlist));
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
      console.log('Response from server:', response.data);
    });

}

async function addTickerToDatabase(ticker, tickerName,tickerType, userId) {
  let params =
  {

    "ticker_code": ticker,
    "ticker_name":tickerName,
    "ticker_type": tickerType,
    "user_id": userId

  };
  let url = 'http://127.0.0.1:5000/send_ticker';


  let response = await axios.post(url, params)
  .then(response => {
    console.log('Response from server:', response);
  });
  // console.log(response)
return console.log('done')
}


window.addEventListener('beforeunload', function() {
  localStorage.clear();
});



document.getElementById('zodiac-signs').addEventListener('change', function() {
  var selectedSign = this.value;
  console.log(selectedSign)
  let url = `http://127.0.0.1:5000/horoscope/${selectedSign}`
  axios.get(url)
  .then(function (response) {

    let reading =document.getElementById('todays-horoscope')
    reading.innerHTML=`${selectedSign} - ${response.data}`
})
.catch(function (error) {
    console.error(error); // Handle errors
});


});


document.getElementById('btn-city').addEventListener('click',getWeather)

function getWeather() {

  let city=document.getElementById('input-city').value
  let url = `http://127.0.0.1:5000/weather/${city}`
  axios.get(url)
  .then(function (response) {
    // let weather=document.getElementById('todays-weather')
    // weather.innerHTML=`${city}-${response.data}`

    let location=response.data.location.name
    let temp=response.data.data.values.temperature
    let humidity=response.data.data.values.humidity
    let precipitation=response.data.data.values.precipitationProbability

    document.getElementById("location").innerHTML=location
    document.getElementById("temp").innerHTML=temp
    document.getElementById("humidity").innerHTML=humidity
    document.getElementById("precipitation").innerHTML=precipitation

    document.getElementById('todays-weather')

})
.catch(function (error) {
    console.error(error); // Handle errors
});



}

async function get_marketSummary(){
  let table = document.getElementById('market-summary');
  url='http://127.0.0.1:5000/market_summary'

  response=await axios.get(url)
  .then(function (response) {

for(let item of response.data){
  var row = table.insertRow();

  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);

  if(item.longName){
    cell1.innerHTML = item.longName;

  } else {
    cell1.innerHTML = item.shortName;
  }
  cell2.innerHTML=item.regularMarketPrice.fmt
  cell3.innerHTML=item.regularMarketChange.fmt
  cell4.innerHTML=item.regularMarketChangePercent.fmt


  }

})

// add listener to reload
}

function get_news(){

  url='http://127.0.0.1:5000/us_news'
  axios.get(url)
  .then(function (response) {

    for (let item of response.data.news){
      console.log(item.link,item.title)
    }
})
.catch(function (error) {
    console.error(error); // Handle errors
});

}





