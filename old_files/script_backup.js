//capture user input
let url = 'http://127.0.0.1:5000/quote/'



async function getQuote() {
let user_input = document.getElementById('ticker')
const ticker =user_input.value.toUpperCase()

try {
     response = await axios.get(url+ticker)

      let price=response.data.regularMarketPrice;
      let name=response.data.shortName
      let change=response.data.regularMarketChange
      let quoteTable= document.getElementById('quote-Table')
      quoteTable.innerHTML = '';
      const newRow = quoteTable.insertRow()
      const cell = newRow.insertCell();
      cell.textContent = ticker + '  '+ name + '  '+ price + '  '+change

      user_input.value=''
      return response

}
 catch {

  user_input.value = '';
  console.log(Promise)
  return console.log('invalid ticker')
 }


    // .catch(error => {
    //   console.error('Error fetching quote:', error);
    // });


}

document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
 const quoteButton = document.getElementById('quote');
 event.preventDefault()

  // Add click event listener to the button
  quoteButton.addEventListener('click', getQuote)


});


function addToWatchlist() {
  let watchlist = JSON.parse(localStorage.getItem('watchlist')) || [];
  const user_input = document.getElementById('ticker');
  const ticker = user_input.value.toUpperCase();

  if (watchlist.includes(ticker)) {
      console.log('Ticker already in watchlist');
      user_input.value = '';
      return;
  }
try {
  watchlist.push(ticker);
  localStorage.setItem('watchlist', JSON.stringify(watchlist));
  console.log('Updated watchlist', watchlist);
  user_input.value = '';
  updateWatchlist(watchlist)

} catch {
  user_input.value = '';
  return console.log('invalid ticker')
}
}

// function updateWatchlist(watchlist){
//   // JSON.parse(localStorage.getItem('watchlist')) || []
//   // Making multiple asynchronous requests
//   Promise.all(watchlist.map(ticker => axios.get('http://127.0.0.1:5000/quote/' + ticker)))
//       .then(responses => {
//           responses.forEach(response => {
//               let price = response.data.regularMarketPrice;
//               let name = response.data.shortName;
//               let change = response.data.regularMarketChange;
//               // Process or display this data as needed
//               console.log(name,price,change)
//           });
//       })
//       .catch(error => {
//           // Handle errors here
//           console.error('Error fetching data:', error);
//       });
//     }



// watchlistTable =document.getElementById('portfolio')
      // const newRow = watchlistTable.insertRow()
      // const cell = newRow.insertCell();
      // cell.textContent = ticker + '  '+ name + '  '+ price + '  '+change
      // let removeButton = document.createElement('button');
      // removeButton.textContent = 'Remove';
      // cell.append(removeButton)
      // removeButton.id='remove'



      // user_input.value=''



    // .catch(error => {
    //   console.error('Error fetching quote:', error);
    //   return 1
    // });





document.addEventListener('DOMContentLoaded', (event) => {
  // Select the button by its ID
 const addTicker = document.getElementById('add');
 event.preventDefault()

  // Add click event listener to the button
  addTicker.addEventListener('click',addToWatchlist )

});



function updateWatchlist(watchlist) {
  watchlist.forEach(ticker => {

    const url = `http://127.0.0.1:5000/quote/${ticker}`;

    axios.get(url)
      .then(response => {

        let price = response.data.regularMarketPrice;
        let name = response.data.shortName;
        let change = response.data.regularMarketChange;



        console.log(`Quote for ${ticker}:`, price , change , name);
        return displayWatchlist(ticker,price,change,name)

        // You can also call a function to update the UI with this quote
      })

      .catch(error => {
        // Handle errors here
        console.error(`Error fetching quote for ${ticker}:`, error);
      });
  } );


}

function displayWatchlist(ticker, price, change, name) {
  let portfolioTable = document.getElementById('portfolio-Table');

  // Create a new row
  let row = document.createElement('tr');

  // Create and append the ticker cell
  let tickerCell = document.createElement('td');
  tickerCell.textContent = ticker;
  row.appendChild(tickerCell);

  // Create and append the price cell
  let priceCell = document.createElement('td');
  priceCell.textContent = price;
  row.appendChild(priceCell);

  // Create and append the change cell
  let changeCell = document.createElement('td');
  changeCell.textContent = change;
  row.appendChild(changeCell);

  // Create and append the name cell
  let nameCell = document.createElement('td');
  nameCell.textContent = name;
  row.appendChild(nameCell);

  // Append the row to the table
  portfolioTable.appendChild(row);
}


















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
