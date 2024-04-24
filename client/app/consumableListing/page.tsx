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
        console.log(data);
        setRes(data);
      })
      .catch((error) => {
        console.log(error.message);
      });
  }, []);

  return (
    <div className="m-6 flex flex-wrap gap-4">
      {res && (
        <div>
          {res.map((consumableListing: any) => {
            return (
              <ConsumableListingCard
                consumable={consumableListing.consumable.name}
                district={consumableListing.district.name}
                postedDate={consumableListing.posted_date}
                price={consumableListing.price}
                quantity={consumableListing.quantity}
                user={consumableListing.user.name}
                userImage={Vegetable}
                consumableImage={`${API_URL}/${consumableListing.consumable.image_path}`}
                consumableType={consumableListing.consumable.type}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}
