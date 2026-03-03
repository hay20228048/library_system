export async function GET() {
  const res = await fetch("http://api:8000/members", {
    cache: "no-store",
  });

  const data = await res.json();
  return Response.json(data);
}