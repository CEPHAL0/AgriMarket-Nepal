"use server";
import { cookies } from "next/headers";
import { RequestMethodsType } from "../lib/definitions";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const fetchWithJwt = async (
  endpoint: string,
  method: RequestMethodsType,
  body?: BodyInit
) => {
  const jwtCookie = cookies().get("jwt");

  if (!jwtCookie) {
    throw new Error("Failed to get jwt");
  }

  const url: string = `${API_URL}${endpoint}`;

  const options: RequestInit = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      Cookie: `${jwtCookie?.value}`,
    },
  };

  if (body) {
    options.body = body;
  }

  return await fetch(url, options);
};
