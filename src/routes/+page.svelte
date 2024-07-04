<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<Card.Root>
		<Card.Header>
			<Card.Title>Epsilon Distribution</Card.Title>
			<Card.Description>A modern music distribution platform.</Card.Description>
		</Card.Header>
		<Card.Content>
			<p>
				Welcome to our exclusive members-only music distribution site, where artists and enthusiasts
				come together to support and celebrate the world of music. As a collective backed by our
				devoted members, we provide a host of benefits designed to amplify your musical reach.
				Membership includes access to exclusive releases, behind-the-scenes content, powerful
				distribution tools, networking opportunities with industry professionals, and invitations to
				private events. Join us and become part of a dynamic community that empowers and elevates
				the art of music distribution.
			</p>
		</Card.Content>
		<Card.Footer>
			<SignedIn>
				<UserButton afterSignOutUrl="/" />
			</SignedIn>
			<SignedOut>
				<Button class="m-2">
					<SignInButton mode="modal">Login</SignInButton>
				</Button>
				<Button class="m-2">
					<SignUpButton mode="modal">Sign up</SignUpButton>
				</Button>
			</SignedOut>
		</Card.Footer>
	</Card.Root>
</section>
