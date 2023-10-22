git <script>
	import { Card, Button } from 'flowbite-svelte';
	import CenterBox from '$lib/CenterBox.svelte';
	import InputGroup from '$lib/InputGroup.svelte';
</script>

<main>
	<CenterBox>
		<Card>
			<form class="mb-6 flex flex-col space-y-4" color="dark">
				<InputGroup inputName="Email" />
				<InputGroup inputName="Password" />
				<Button outline type="submit">Login</Button>
			</form>
		</Card>
	</CenterBox>
</main>
