<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
	import Typewriter from 'svelte-typewriter';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
</script>

<Card.Root class="m-4 w-3/5 max-w-xl">
	<Card.Header>
		<Card.Title>Epsilon FM</Card.Title>
		<Card.Description
			>The modern open-source music business platform for industry professionals.</Card.Description
		>
	</Card.Header>
	<SignedOut>
		<Card.Content>
			<Typewriter mode="loopOnce" interval={100} cursor={true} keepCursorOnFinish={true}>
				<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">
					Goodbye DistroKid.
				</h4>
				<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">
					Hello Epsilon FM.
				</h4>
				<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">
					Welcome to the future.
				</h4>
			</Typewriter>
		</Card.Content>
	</SignedOut>
	<Card.Content>
		<SignedIn>
			<div class="flex flex-row justify-between">
				<Button href="/dashboard" class="m-2">👈 Back to Dashboard</Button>
				<div class="m-2 pt-1">
					<UserButton />
				</div>
			</div>
		</SignedIn>
		<SignedOut>
			<Button class="m-2">
				<SignInButton>Login</SignInButton>
			</Button>
			<Button class="m-2">
				<SignUpButton>Sign up</SignUpButton>
			</Button>
		</SignedOut>
	</Card.Content>
</Card.Root>
