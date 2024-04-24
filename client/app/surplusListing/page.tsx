"use client";

import ConsumableListingCard from "@/components/ConsumableListings/ConsumableListingCard";
import { useState, useEffect } from "react";
import Vegetable from "@/public/Vegetables.jpg";
import { fetchSurplusListings } from "./fetchSurplusListing";

export default function Page() {
  const [res, setRes] = useState<any>();

  useEffect(() => {
    fetchSurplusListings()
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
                key={consumableListing.id}
                consumable={consumableListing.consumable.name}
                district={consumableListing.district.name}
                postedDate={consumableListing.posted_date}
                price={consumableListing.price}
                quantity={consumableListing.quantity}
                user={consumableListing.user.name}
                userImage={Vegetable}
                consumableImage={Vegetable}
                consumableType={consumableListing.consumable.type}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}
