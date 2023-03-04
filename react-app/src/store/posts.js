const GET_ALL_POSTS = 'coffee/GET_ALL_POSTS'
const GET_A_POST = 'coffee/GET_A_POST'
const ADD_A_POST = 'coffee/ADD_A_POST'
const DELETE_A_POST = 'coffee/DELETE_A_POST'

const setPosts = (posts) => ({
  type: GET_ALL_POSTS,
  ...posts
})

const setPost = (post) => ({
  type: GET_A_POST,
  ...post
})

const addPost = (post) => ({
  type: ADD_A_POST,
  ...post
})

const deletePost = (postId) => ({
  type: DELETE_A_POST,
  postId
})


export const fetchPosts = () => async dispatch => {
  const res = await fetch(`/api/post/`)

  if (res.ok) {
    const posts = await res.json()
    dispatch(setPosts(posts))

    return posts
  }
}

export const fetchPost = (postId) => async dispatch => {
  const res = await fetch(`/api/post/${postId}`)

  if (res.ok) {
    const post = await res.json()
    dispatch(setPost(post))

    return post
  }
}

export const fetchAddPost = (post) => async dispatch => {
  const res = await fetch(`/api/post/`, {
    methods: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(post)
  })

  if (res.ok) {
    const newPost = await res.json()
    dispatch(addPost(newPost))

    return newPost
  }
}

export const fetchDeletePost = (postId) => async dispatch => {
  const res = await fetch(`/api/post/${postId}`, {
    methods: "DELETE"
  })

  if (res.ok) {
    dispatch(deletePost(postId))

    return { "message": "Successfully Deleted Post. Good Bye, Brain Stew!" }
  }
}

const initialState = { posts: {}, onePost: {} }

export default function reducer(state = initialState, action) {
  switch (action.type) {

    case GET_ALL_POSTS: {
      const loadState = { ...state, posts: { ...state.posts }, onePost: { ...state.onePost } }
      action.posts.forEach(post => {
        loadState.posts[post.id] = post;
      })

      return loadState
    }

    case GET_A_POST: {
      const loadState = { ...state, posts: { ...state.posts }, onePost: { ...state.onePost } }
      loadState.onePost = action.post

      return loadState
    }

    case ADD_A_POST: {
      const addedState = { ...state, posts: { ...state.posts }, onePost: { ...state.onePost } }
      addedState.posts[action.post.id] = action.post
    }

    case DELETE_A_POST: {
      const deletedState = { ...state, posts: { ...state.posts }, onePost: { ...state.onePost } }
      delete deletedState.posts[action.postId]

      return deletedState
    }

    default:
      return state
  }
}
