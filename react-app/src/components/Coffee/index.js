import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchCoffee } from '../../store/coffee'


export default function Coffee() {
  const [isLoaded, setIsLoaded] = useState(false)
  const [coffeeList, setCoffeeList] = useState([])
  const dispatch = useDispatch()
  const coffee = useSelector(state => state.coffee.coffee)

  useEffect(() => {
    if (!isLoaded) {
      dispatch(fetchCoffee())
        .then(() => {
          setCoffeeList(Object?.values(coffee))
        })
        .then(() => setIsLoaded(true))
    }
  }, [dispatch, coffeeList])

  if (!isLoaded) return 'Loading...!'

  return (
    <div>
      HERE WILL BE COFFEE
      <div>
        {coffeeList.length}
      </div>
    </div>
  )
}
