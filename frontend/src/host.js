export const HOST =
  process.env.NODE_ENV === "production"
    ? ""
    : "http://127.0.0.1:8000";