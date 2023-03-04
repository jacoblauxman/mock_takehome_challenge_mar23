import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchPosts } from '../../store/posts'

export default function Posts() {

  const [isLoaded, setIsLoaded] = useState(false)
  const [postsList, setPostsList] = useState([])
  const dispatch = useDispatch()
  const posts = useSelector(state => state.posts.posts)

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
      {posts && postsList.forEach(post => (
        <div>
          <div>{post?.title}</div>
          <div>{postsList.length}</div>
          <div>{post?.text}</div>
          {console.log(post.title, 'TESTING FOR POST!!')}
        </div>
      ))}

    </div>
  )
}
