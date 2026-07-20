"use client";

import { useEffect } from "react";
import Clarity from "@microsoft/clarity";

const CLARITY_PROJECT_ID = "xpaxtyp60x";

let clarityInitialized = false;

export default function ClarityAnalytics() {
  useEffect(() => {
    if (process.env.NODE_ENV !== "production" || clarityInitialized) return;
    clarityInitialized = true;
    Clarity.init(CLARITY_PROJECT_ID);
  }, []);

  return null;
}
