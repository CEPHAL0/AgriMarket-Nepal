import { z } from 'zod'

export const SignInSchema = z.object({
  username: z.string().min(3, 'Username is required'),
  password: z.string().min(1, 'Password is required')
})

export type TSignInSchema = z.infer<typeof SignInSchema>

export type FormState =
  | {
      errors?: {
        name?: string[]
        password?: string[]
      }
      message?: string
      error?: string
    }
  | undefined
