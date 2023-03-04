import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchPosts } from '../../store/posts'

export default function Posts() {

  const [isLoaded, setIsLoaded] = useState(false)
  const [postsList, setPostsList] = useState([])
  const dispatch = useDispatch()
  const posts = useSelector(state => state.posts.posts)
  console.log(posts, 'POSTS IN OUR POSTS COMPONENT', postsList, "AND POSTSLISTS TO COMPARE")

  useEffect(() => {
    if (!isLoaded) {
      dispatch(fetchPosts())
        .then(() => {
          setPostsList(Object?.values(posts))
        })
        .then(() => setIsLoaded(true))
    }
  }, [dispatch, postsList])

  if (!isLoaded) return 'Loading...!'

  return (
    <div>
      {postsList.length}
      {posts && postsList.length > 0 && postsList.forEach(p => (
        <div>
          <div>{p?.title}</div>
          <div>{postsList.length}</div>
          <div>{p?.text}</div>
          {console.log(p.title, 'TESTING FOR POST!!')}
        </div>
      ))}

    </div>
  )
}
