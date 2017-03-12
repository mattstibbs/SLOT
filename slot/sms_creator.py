import logging
log = logging.getLogger('slot')


def new_procedure_message(procedure, location, expiry_time, doctor, message_ref):
    message = str.format("{0} at {1}.\nAttend by {2}.\nAsk for {3}.\n\nTo accept reply '{4}'",
                         procedure,
                         location,
                         expiry_time,
                         doctor,
                         message_ref)
    log_message(message)
    return message


def success_response_message(procedure, location, duration, doctor):
    message = str.format("Please attend {0} in {1} and ask for {2} to complete this supervised "
                         "procedure. This learning opportunity has been reserved exclusively for you, please make "
                         "every effort to attend.",
                         location,
                         duration,
                         doctor)
    log_message(message)
    return message


def not_successful_response_message():
    message = str.format("Sorry - procedure already taken this time.")
    log_message(message)
    return message


def log_message(message):
    log.debug("Generated message:\n {0}".format(message))