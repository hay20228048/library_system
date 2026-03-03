async function getMembers() {
  const res = await fetch("http://localhost:3000/api/members", {
    cache: "no-store",
  });

  return res.json();
}

export default async function MembersPage() {
  const members = await getMembers();

  return (
    <div>
      <h1>Members</h1>
      <ul>
        {members.map((member: any) => (
          <li key={member.member_id}>
            {member.name}
          </li>
        ))}
      </ul>
    </div>
  );
}