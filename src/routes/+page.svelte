<script lang="ts">
  import { superForm } from 'sveltekit-superforms';
  import { Button } from 'svelte-ux';
  import { ThemeSelect, Card } from 'svelte-ux';

  export let data;

  // Client API:
  const { form } = superForm(data.form);

</script>
<Card title="Title" subheading="Subheading" />
<!-- <Button>Click here</Button>
<ThemeSelect lightThemes={["light"]} darkThemes={["dark"]} />
<div class="card p-4">  
    Welcome to our exclusive members-only music distribution site, where artists and enthusiasts come together to support and celebrate the world of music. As a collective backed by our devoted members, we provide a host of benefits designed to amplify your musical reach. Membership includes access to exclusive releases, behind-the-scenes content, powerful distribution tools, networking opportunities with industry professionals, and invitations to private events. Join us and become part of a dynamic community that empowers and elevates the art of music distribution.
</div>
<form method="POST">
  <label for="name">Name</label>
  <input type="text" name="name" bind:value={$form.name} />

  <label for="email">E-mail</label>
  <input type="email" name="email" bind:value={$form.email} />

  <div><button>Submit</button></div>
</form> -->