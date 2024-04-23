"use server";

import { redirect } from "next/navigation";
import { NextResponse } from "next/server";
import { SignInSchema, FormState, TSignInSchema } from "../lib/definitions";
import { createSession } from "../lib/session";
import { isRedirectError } from "next/dist/client/components/redirect";
import { cookies } from "next/headers";
import { fetchWithJwt } from "../utils/fetchWithJwt";

export const signIn = async (state: FormState, formData: FormData) => {
  const validateFields = SignInSchema.safeParse({
    username: formData.get("username"),
    password: formData.get("password"),
  });

  if (!validateFields.success) {
    return { errors: validateFields.error.flatten().fieldErrors };
  }

  const { username, password } = validateFields.data;
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    const jsonData = await response.json();
    if (!response.ok) {
      return {
        error: jsonData.detail,
      };
    }
    if (response.status != 200) {
      return {
        error: "Invalid credentials",
      };
    }
    await createSession(jsonData.access_token);
    redirect("/");
  } catch (err: any) {
    if (isRedirectError(err)) {
      redirect("/");
    }
    console.log(err);
  }
};

export async function handleClick() {
  try {
    const myCookie = cookies();
    const jwtCookie = myCookie.get("jwt");
    // const myresponse = await fetch(
    //   `${process.env.NEXT_PUBLIC_API_URL}/consumables`,
    //   {
    //     method: "GET",
    //     headers: {
    //       "Content-Type": "application/json",
    //       Cookie: `${jwtCookie?.value}`,
    //     },
    //   }
    // );

    const response = await fetchWithJwt("/consumables", "GET");

    const res = await response.json();
    console.log(res);
  } catch (e: any) {
    console.log(e.message);
  }
}
