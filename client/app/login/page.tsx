'use client'

import React, { useEffect } from 'react'
import { TSignInSchema } from '../lib/definitions'

import { signIn } from '../actions/auth'
import { useFormState, useFormStatus } from 'react-dom'
import { useToast } from '@/components/ui/use-toast'

const Login = () => {
  const [state, action] = useFormState(signIn, undefined)
  const { toast } = useToast()
  const { pending } = useFormStatus()
  const onSubmit = async (data: TSignInSchema) => {
    try {
      const response: Response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/login`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ ...data })
        }
      )
      const responseData = await response.json()
      document.cookie = `jwt=${responseData.access_token}`
      console.log(data)
    } catch (err) {
      console.log(err)
    }
  }

  async function handleClick() {
    try {
      const response: Response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/users`,
        {
          credentials: 'include',
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        }
      )

      const data = await response.json()

      console.log(data)
    } catch (err) {
      console.log(err)
    }
  }

  console.log(state?.error)

  useEffect(() => {
    toast({
      variant: 'destructive',
      description: state?.error
    })
  }, [state?.error, toast])

  return (
    <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
      <button onClick={handleClick}>Click Me</button>
      <div className="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
          Sign in to your account
        </h2>
      </div>

      <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form className="space-y-6" action={action}>
          <div>
            <label className="block text-sm font-medium leading-6 text-gray-900">
              User Name
            </label>
            <div className="mt-2">
              <input
                id="username"
                type="text"
                name="username"
                className="block w-full rounded-md border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
              {state?.errors && (
                <p className="text-red-600">{state.errors.username}</p>
              )}
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between">
              <label className="block text-sm font-medium leading-6 text-gray-900">
                Password
              </label>
              <div className="text-sm">
                <a
                  href="#"
                  className="font-semibold text-indigo-600 hover:text-indigo-500"
                >
                  Forgot password?
                </a>
              </div>
            </div>
            <div className="mt-2">
              <input
                id="password"
                type="password"
                name="password"
                className="block w-full rounded-md border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
              {state?.errors && (
                <p className="text-red-600">{state.errors.password}</p>
              )}
            </div>
          </div>

          <div>
            <button
              type="submit"
              aria-disabled={pending}
              className={`flex w-full justify-center rounded-md  px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 
                bg-indigo-600
              `}
            >
              {pending ? 'Submitting...' : 'Submit'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Login
