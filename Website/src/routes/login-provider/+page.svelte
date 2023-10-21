<script>
	import { Input, Label, Card, Button } from 'flowbite-svelte';
	import CenterBox from '$lib/CenterBox.svelte';
</script>

<main>
	<CenterBox>
		<Card>
			<form class="mb-6 flex flex-col space-y-4" color="dark">
				<Label for="default-input" class="block mb-2">Email</Label>
				<Input id="default-input" class="email" placeholder="email" />
				<Label for="default-input" class="block mb-2">Password</Label>
				<Input id="default-input" class="password" placeholder="password" />
				<Button outline type="submit">Login</Button>
			</form>
		</Card>
	</CenterBox>
</main>
