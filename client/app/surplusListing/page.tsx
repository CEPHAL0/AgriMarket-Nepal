"use client";

import ConsumableListingCard from "@/components/ConsumableListings/ConsumableListingCard";
import { useState, useEffect } from "react";
import Vegetable from "@/public/Vegetables.jpg";
import { fetchSurplusListings } from "./fetchSurplusListing";
import { SurplusListing } from "@/types/types";
import SurplusListingCard from "@/components/SurplusListing/SurplusListing";

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
          {res.map((surplusListing: SurplusListing) => {
            return (
              <div className="m-8" key={surplusListing.id}>
                <SurplusListingCard
                  booked={surplusListing.booked}
                  consumable={surplusListing.consumable}
                  farmer={surplusListing.farmer}
                  price={surplusListing.price}
                />
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
