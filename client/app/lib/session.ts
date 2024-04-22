import 'server-only'
import { cookies } from 'next/headers'

export const createSession = async (accessToken: string) => {
  cookies().set('jwt', `jwt=${accessToken}`)
}
