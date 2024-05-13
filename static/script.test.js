import axios from 'axios-mock-adapter';
describe('api exists', () => {

  it('GET /info should return 200 response', (done) => {
    axios.get("http://127.0.0.1:5000/quote/AAPL")
     .then((response) => {
       console.log(response);
       expect(response.statusCode).toBe(200);
       done();
     })
  });
});