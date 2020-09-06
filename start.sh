#!/bin/bash

case "${1}" in
	client|c)
		shift
		exec python client.py ${@}
	;;
	server|s)
		shift
		exec python server.py ${@}
	;;
	*)
		exec python server.py ${@}
	;;
esac

