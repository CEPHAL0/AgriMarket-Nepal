"use client";

import ConsumableCard from "@/components/Consumables/ConsumableCard";
import ConsumableListingCard from "@/components/ConsumableListings/ConsumableListingCard";
import { cookies } from "next/headers";
import Vegetable from "@/public/Vegetables.jpg";
import { handleClick } from "../actions/auth";
export default async function Page() {
  return (
    <div className="m-6 flex flex-wrap gap-4">
      <ConsumableCard image={Vegetable} name="Radish" type="VEGETABLE" />
      <ConsumableCard image={Vegetable} name="Apple" type="FRUIT" />
      <ConsumableCard image={Vegetable} name="Milk" type="OTHER" />
      <ConsumableListingCard
        consumable="Radish"
        district="Banepa"
        postedDate="2014-10-21"
        price={400}
        quantity={450.45}
        user="Sharad Sharma"
        userImage={Vegetable}
        consumableImage={Vegetable}
        consumableType="FRUIT"
      />
      <button
        onClick={async () => {
          await handleClick();
        }}
      >
        Click Me
      </button>
    </div>
  );
}
