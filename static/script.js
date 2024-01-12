//capture user input

const watchlist =[]

function getQuote() {
let user_input = document.getElementById('ticker')
const ticker =user_input.value.toUpperCase()

  let quoteUrl = 'http://127.0.0.1:5000/quote/' + ticker;
     axios.get(quoteUrl)
    .then(response => {
      let price=response.data.regularMarketPrice;
      let name=response.data.shortName
      let change=response.data.regularMarketChange
      let quoteTable= document.getElementById('quote-Table')
      quoteTable.innerHTML = '';
      const newRow = quoteTable.insertRow()
      const cell = newRow.insertCell();
      cell.textContent = ticker + '  '+ name + '  '+ price + '  '+change
      let addButton = document.createElement('button');
      addButton.textContent = 'Add to Watchlist';
      cell.append(addButton)
      user_input.value=''



    })
    .catch(error => {
      console.error('Error fetching quote:', error);
    });


}

document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
 const quoteButton = document.getElementById('quote');
 event.preventDefault()

  // Add click event listener to the button
  quoteButton.addEventListener('click', function() {
      getQuote(); // Call the getQuote function
  });
});


function addToWatchlist(){

  const user_input = document.getElementById('ticker')
  const ticker =user_input.value.toUpperCase()
  let quoteUrl = 'http://127.0.0.1:5000/quote/' + ticker;
     axios.get(quoteUrl)
    .then(response => {
      let price=response.data.regularMarketPrice;
      let name=response.data.shortName
      let change=response.data.regularMarketChange

      let watchlistTable =document.getElementById('watchList-Table')
      const newRow = watchlistTable.insertRow()
      const cell = newRow.insertCell();
      cell.textContent = ticker + '  '+ name + '  '+ price + '  '+change
      let addButton = document.createElement('button');
      addButton.textContent = 'Remove';
      cell.append(addButton)

      user_input.value=''



    })
    .catch(error => {
      console.error('Error fetching quote:', error);
    });

}


document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
 const quoteButton = document.getElementById('add');
 event.preventDefault()

  // Add click event listener to the button
  quoteButton.addEventListener('click', function() {
      addToWatchlist(); // add to watchlist
  });
});



// function addTicker() {
//   const ticker = document.getElementById('stockTicker').value;
//   axios.post('/quote', { ticker })
//       .then(() => updateWatchlist())
//       .catch(error => console.error(error));
// }

// function removeTicker() {
//   const ticker = document.getElementById('stockTicker').value;
//   axios.post('/api/stock/remove', { ticker })
//       .then(() => updateWatchlist())
//       .catch(error => console.error(error));
// }

// function updateWatchlist() {
//   axios.get('/api/stock/get')
//       .then(response => {
//           const watchlist = response.data.watchlist.map(item => item[0]).join(', ');
//           document.getElementById('watchlist').innerText = watchlist;
//       })
//       .catch(error => console.error(error));
// }

// // Initial watchlist update
// updateWatchlist();
// let counter=15;

// function updatePortfolio(){

//   let countdown = setInterval(function(){
//     counter --;
//     console.log(counter)
//     if(counter <=1){
//       //remove this when constand polling
//       clearInterval(countdown);
//     }


//   },1000)
// }

// let stockTickers = [];

// // Function to add a ticker to the array
// function addTicker(newTicker) {
//     // Check if the ticker is already in the array
//     if (!stockTickers.includes(newTicker)) {
//         stockTickers.push(newTicker); // Add the new ticker
//     } else {
//         console.log("Ticker already exists in the portfolio.");
//     }
// }

// // Example usage
// addTicker("AAPL"); // Adding Apple Inc. ticker
// addTicker("MSFT"); // Adding Microsoft Corp. ticker

//add Ticker to portfolio
//user enters ticker into form
//user clicks 'add' to watchlist
//ticker is added to watchlist array





//loop through the watchlist
//call backend to write ticker to db
//call quote endpoint to receive quotes every 15 seconds
