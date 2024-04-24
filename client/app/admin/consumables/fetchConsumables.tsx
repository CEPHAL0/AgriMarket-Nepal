"use server";

import { fetchWithJwt } from "@/app/utils/fetchWithJwt";
import { cookies } from "next/headers";

export async function fetchConsumables() {
  try {
    //   const myCookie = cookies();
    //   const jwtCookie = myCookie.get("jwt");
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

    console.log("status: ", response.ok);

    if (response.ok) {
      const res = await response.json();
      return res;
    } else {
      //   console.log(response);
      //   return "error";
      return;
    }
    // console.log("status: ", res.status);

    // console.log(res);
    // return res;
  } catch (e: any) {
    console.log(e.message);
    return e;
  }
}
