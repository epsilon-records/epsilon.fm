<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import github from '$lib/images/github.svg';
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
				Experience unlimited music distribution with our modern open-source platform for just
				$99/year, including features like an artist website, social media management, and merch,
				empowering you with global reach and full control over your creative work.
			</p>
		</Card.Content>
		<Card.Footer>
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
