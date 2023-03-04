const GET_ALL_COFFEE = 'coffee/GET_ALL_COFFEE'
const GET_A_COFFEE = 'coffee/GET_A_COFFEE'
const ADD_A_COFFEE = 'coffee/ADD_A_COFFEE'
const DELETE_A_COFFEE = 'coffee/DELETE_A_COFFEE'

const setCoffees = (coffees) => ({
  type: GET_ALL_COFFEE,
  ...coffees
})

const setCoffee = (coffee) => ({
  type: GET_A_COFFEE,
  ...coffee
})

const addCoffee = (coffee) => ({
  type: ADD_A_COFFEE,
  ...coffee
})

const deleteCoffee = (coffeeId) => ({
  type: DELETE_A_COFFEE,
  coffeeId
})


export const fetchCoffee = () => async dispatch => {
  const res = await fetch(`/api/coffee/`)

  if (res.ok) {
    const coffees = await res.json()
    dispatch(setCoffees(coffees))

    return coffees
  }
}

export const fetchACoffee = (coffeeId) => async dispatch => {
  const res = await fetch(`/api/coffee/${coffeeId}`)

  if (res.ok) {
    const coffee = await res.json()
    dispatch(setCoffee(coffee))

    return coffee
  }
}

export const fetchAddCoffee = (coffee) => async dispatch => {
  const res = await fetch(`/api/coffee/create`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(coffee)
  })

  if (res.ok) {
    const newCoffee = await res.json()
    dispatch(addCoffee(newCoffee))

    return newCoffee
  }
}

export const fetchDeleteCoffee = (coffeeId) => async dispatch => {
  const res = await fetch(`/api/coffee/${coffeeId}`, {
    method: "DELETE"
  })

  if (res.ok) {
    dispatch(deleteCoffee(coffeeId))

    return { "message": "Successfully Deleted Coffee. Good Bye, Bean Juice!" }
  }
}


const initialState = { coffee: {}, oneCoffee: {} }

export default function reducer(state = initialState, action) {
  switch (action.type) {

    case GET_ALL_COFFEE: {
      const loadState = { ...state, coffee: { ...state.coffee }, oneCoffee: { ...state.oneCoffee } }
      action.coffees.forEach(coffee => {
        loadState.coffee[coffee.id] = coffee;
      })

      return loadState
    }

    case GET_A_COFFEE: {
      const loadState = { ...state, coffee: { ...state.coffee }, oneCoffee: { ...state.oneCoffee } }
      loadState.oneCoffee = action.coffee

      return loadState
    }

    case ADD_A_COFFEE: {
      const addedState = { ...state, coffee: { ...state.coffee }, oneCoffee: { ...state.oneCoffee } }
      addedState.coffee[action.coffee.id] = action.coffee
    }

    case DELETE_A_COFFEE: {
      const deletedState = { ...state, coffee: { ...state.coffee }, oneCoffee: { ...state.oneCoffee } }
      delete deletedState.coffee[action.coffeeId]

      return deletedState
    }

    default:
      return state;
  }
}
