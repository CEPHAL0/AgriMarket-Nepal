"use client";

import React, { useEffect } from "react";
import { TSignInSchema } from "@/app/lib/definitions";

import { signIn } from "@/app/actions/auth";
import { useFormState, useFormStatus } from "react-dom";
import { useToast } from "@/components/ui/use-toast";
import Link from "next/link";

export default function LoginForm() {
  const [state, action] = useFormState(signIn, undefined);
  const { toast } = useToast();
  const { pending } = useFormStatus();

  useEffect(() => {
    toast({
      variant: "destructive",
      description: state?.error,
    });
  }, [state?.error, toast]);

  return (
    <form className="space-y-6" action={action}>
      <div>
        <label className="block text-sm font-medium  text-gray-900">
          Username
        </label>
        <div className="mt-2">
          <input
            id="username"
            type="text"
            name="username"
            className="block w-full rounded-md border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-green sm:text-sm sm:leading-6"
          />
          {state?.errors && (
            <p className="text-primary-red text-xs mt-1">
              {state.errors.username}
            </p>
          )}
        </div>
      </div>

      <div>
        <div className="flex items-center justify-between">
          <label className="block text-sm font-medium text-gray-900">
            Password
          </label>
        </div>
        <div className="mt-2 flex flex-col gap-2">
          <input
            id="password"
            type="password"
            name="password"
            className="block w-full rounded-md border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary-green sm:text-sm sm:leading-6"
          />
          {state?.errors && (
            <p className="text-primary-red text-xs mt-1">
              {state.errors.password}
            </p>
          )}

          <div className="text-sm self-end">
            <a
              href="#"
              className="font-normal text-xs text-primary-green hover:text-primary-red"
            >
              Forgot password?
            </a>
          </div>
        </div>
      </div>

      <div>
        <button
          type="submit"
          aria-disabled={pending}
          className={`flex w-full justify-center rounded-md px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-primary-blue focus-visible:outline 
          focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-secondary-green 
                bg-primary-green
              `}
        >
          {pending ? "Logging In..." : "Login"}
        </button>
      </div>

      <div className="text-center text-sm">
        Don't have an account?{" "}
        <Link href="/register">
          <span className="text-primary-blue font-bold">Signup</span>
        </Link>
      </div>
    </form>
  );
}
