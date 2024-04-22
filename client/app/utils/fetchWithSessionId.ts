import { cookies } from 'next/headers'

const API_URL = process.env.NEXT_PUBLIC_API_URL

export const fetchWithSessionId = async (
  endpoint: string,
  init: RequestInit
) => {
  const sessionId = cookies().get('jwt')
  const url: string = `${API_URL}${endpoint}`

  const options: RequestInit = {
    ...init,
    headers: {
      ...init.headers,
      jwt: `Bearer ${sessionId}`
    }
  }

  try {
    return await fetch(url, options)
  } catch (err) {
    console.error(err)
    throw err
  }
}
