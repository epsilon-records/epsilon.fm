<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button/index';
	import SignInButton from 'clerk-sveltekit/client/SignInButton.svelte';
	import SignUpButton from 'clerk-sveltekit/client/SignUpButton.svelte';
	import Typewriter from 'svelte-typewriter';
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>Epsilon FM</Card.Title>
		<Card.Description>A modern open-source music business platform.</Card.Description>
	</Card.Header>
	<Card.Content>
		<Typewriter mode="scramble" scrambleSlowdown={true} keepCursorOnFinish={true}>
			<h4 class="scroll-m-20 text-center text-4xl font-semibold tracking-tight">Welcome</h4>
		</Typewriter>
	</Card.Content>
	<Card.Content>
		<Button class="m-2">
			<SignInButton mode="modal">Login</SignInButton>
		</Button>
		<Button class="m-2">
			<SignUpButton mode="modal">Sign up</SignUpButton>
		</Button>
	</Card.Content>
</Card.Root>
