"use client";

import ConsumableListingCard from "@/components/ConsumableListings/ConsumableListingCard";
import { useState, useEffect } from "react";
import Vegetable from "@/public/Vegetables.jpg";
import { fetchConsumableListings } from "./fetchConsumableListing";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function Page() {
  const [res, setRes] = useState<any>();

  useEffect(() => {
    fetchConsumableListings()
      .then((data) => {
        setRes(data);
      })
      .catch((error) => {
        console.log(error.message);
      });
  }, []);

  return (
    <div className="px-4 py-6 flex flex-col items-center justify-center gap-8">
      <h1 className="text-4xl font-bold">
        <span className="text-primary-green">Consumbale </span> Listings
      </h1>
      {res ? (
        <div className="flex flex-wrap justify-center gap-10 w-full">
          {res.map((consumableListing: any) => {
            return (
              <ConsumableListingCard
                key={consumableListing.id}
                consumable={consumableListing.consumable.name}
                district={consumableListing.district.name}
                postedDate={consumableListing.posted_date}
                price={consumableListing.price}
                quantity={consumableListing.quantity}
                user={consumableListing.user.name}
                userImage={`${API_URL}/${consumableListing.user.image}`}
                consumableImage={`${API_URL}/${consumableListing.consumable.image_path}`}
                consumableType={consumableListing.consumable.type}
              />
            );
          })}
        </div>
      ) : (
        "Loading..."
      )}
    </div>
  );
}
