
//C:\Users\lachl\dalai\alpaca\models\7B
const Dalai = require('dalai')
const dalai = new Dalai()
const chars = `h llo there`

const sampleString = `TEST`

dalai.request(
    {
        model: "alpaca.7B",
        prompt: `Parse "${chars}" into a sentence.`
    },
    (token) => {
        console.log("TEST")
        console.log(token)
    }
)

console.log("end test")