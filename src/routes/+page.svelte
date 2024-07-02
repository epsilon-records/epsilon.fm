<script>
	import { superForm } from 'sveltekit-superforms';
	import { Button } from 'svelte-ux';
	import { ThemeSelect, Card } from 'svelte-ux';

	export let data;

	// Client API:
	const { form } = superForm(data.form);

</script>

<main class="p-2 grid place-items-center content-center">

	<Card title="Epsilon Distribution" subheading="A modern music distribution platform." />
	<div class="card p-4">  
		Welcome to our exclusive members-only music distribution site, where artists and enthusiasts come together to support and celebrate the world of music. As a collective backed by our devoted members, we provide a host of benefits designed to amplify your musical reach. Membership includes access to exclusive releases, behind-the-scenes content, powerful distribution tools, networking opportunities with industry professionals, and invitations to private events. Join us and become part of a dynamic community that empowers and elevates the art of music distribution.
	</div>
</main>
