"use server";

import { fetchWithJwt } from "../utils/fetchWithJwt";

export async function fetchSurplusListings() {
  try {
    const response = await fetchWithJwt("/surplusListings", "GET");
    if (!response.ok) {
      throw new Error("Failed to get response");
    }
    const res = await response.json();
    return res;
  } catch (e: any) {
    throw new Error("Failed to get message");
  }
}
