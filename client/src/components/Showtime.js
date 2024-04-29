import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

const Showtime = ({ movieId, onSubmit }) => {
  // Form validation schema
  const validationSchema = Yup.object().shape({
    time: Yup.date().required('Time is required'),
  });

  const handleSubmit = async (values, { resetForm }) => {
    try {
      const response = await axios.post(`/movies/${movieId}/showtimes`, values);
      onSubmit(response.data);
      resetForm();
    } catch (error) {
      console.error('Error adding showtime:', error);
    }
  };

  return (
    <div>
      <h2>Add Showtime</h2>
      <Formik
        initialValues={{ time: '' }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            <div className="form-group">
              <label htmlFor="time">Time:</label>
              <Field type="datetime-local" name="time" className="form-control" />
              <ErrorMessage name="time" component="div" className="text-danger" />
            </div>
            <button type="submit" className="btn btn-primary" disabled={isSubmitting}>Add Showtime</button>
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default Showtime;
