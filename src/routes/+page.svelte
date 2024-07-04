<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
	import partners from '$lib/images/partners.png';
	import { Badge } from '$lib/components/ui/badge/index';
</script>

<svelte:head>
	<title>Epsilon Distribution</title>
	<meta
		name="description"
		content="Our modern open-source platform includes features like an artist website, social media management, and merch, empowering you with global reach and full control over your creative work."
	/>
</svelte:head>

<section>
	<Card.Root>
		<Card.Header>
			<Card.Title>Epsilon Distribution</Card.Title>
			<Card.Description>A modern open-source music distribution platform.</Card.Description>
		</Card.Header>
		<Card.Content>
			<p>Experience unlimited music distribution for just <Badge>$99/year</Badge></p>
			<SignedOut>
				<Button class="m-2">
					<SignInButton mode="modal">Login</SignInButton>
				</Button>
				<Button class="m-2">
					<SignUpButton mode="modal">Sign up</SignUpButton>
				</Button>
			</SignedOut>
		</Card.Content>
		<Card.Content>
			<p>
				Our modern open-source platform includes features like an artist website, social media
				management, and merch, empowering you with global reach and full control over your creative
				work.
			</p>
		</Card.Content>
		<Card.Content>
			<p>
				We collaborate with top music industry companies to deliver the ultimate experience for you.
			</p>
			<img alt="Epsilon Distribution Partners" src={partners} />
		</Card.Content>
		<Card.Footer></Card.Footer>
	</Card.Root>
</section>
